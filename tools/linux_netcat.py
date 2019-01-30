#!/usr/bin/python

# ========================================================================
# =====================           NetCat          ========================
# ========================================================================
# 系统模块
import sys
# socket 模块
import socket
# 线程模块
import threading
# 命令行选项得C风格解析器
import getopt
# 子流程管理模块
import subprocess

# ==========  全局变量  ==========

listen                = False
command               = False
upload                = False
execute               = ""
target                = ""
upload_destination   = ""
port                  = ""
# ================================

def usage():
  print("Net Cat Tool\n")
  print("Usage: netcat.py -t target_host -p port\n")
  print("-l --listen                - listen on [host]:[port] incoming connections")
  print("-e --execute=file_to_run   - execute the given file upon receiving a connection")
  print("-c --command               - initialize a command shell")
  print("-u --upload=destination    - upon receiving connection upload a file and write to [destination]\n\n")
  print("Examples:")
  print("netcat.py -t 127.0.0.1 -p 8080 -l -c")
  print("netcat.py -t 127.0.0.1 -p 8080 -l -u=C:\\target.exe")
  print("netcat.py -t 127.0.0.1 -p 8080 -l -e=\"cat /etc/passwd\"")
  print("echo 'ABCDEF' | ./netcat.py -t 127.0.0.1 -p 135")
  try:
    sys.exit(0)
  except:
    print()
    


def main():
  global listen
  global command
  global upload
  global execute
  global target
  global upload_destination
  global port

  if not len(sys.argv[1:]):
    usage()

  # 读取命令行选项
  try:
    opts,args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",["help", "listen", "execute","target", "port","command","upload"])
  except getopt.GetoptError as error:
    print(error)
    usage()

  for o,a in opts:
    if o in ("-h","--help"):
      usage()
    elif o in ("-l","--listen"):
      listen = True
    elif o in ("-e","--execute"):
      execute = True
    elif o in ("-c","--commandshell"):
      command = True
    elif o in ("-u","--upload"):
      upload_destination = a
    elif o in ("-t","--target"):
      target = a
    elif o in ("-p","port"):
      port = int(a)
    else:
      assert False,"unhandled Option"

  # 判断是进行监听还是仅发送数据
  if not listen and len(target) and port > 0:

    # 读取命令行中的内存数据
    # 这里阻塞，不在向标准输入发送数据时发送CTRL-D
    buffer = sys.stdin.readline()
    print(buffer)
    # 发送数据
    client_sender(buffer)
  # 开始监听并准备上传文件或执行命令
  # 放置一个反弹shell
  # 命令取决于上边的命令行选项
  if listen:
    server_loop()



def client_sender(buffer):
  client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  try:
    # 连接到目标主机
    client.connect((target,port))
    # 如果有数据则发送数据
    if len(buffer):
      client.send(buffer.encode())
    while True:

      # 等待数据回传
      recv_len = 1
      response = ""
      while recv_len:
        data = client.recv(4096)
        recv_len = len(data)
        response = data
        if recv_len < 4096:
          break
      
      print(response.decode())

      # 等待更多的输入
      buffer = input("")
     
      buffer += "\n"
      client.send(buffer.encode())

  except:
    print("[*] Exception! Exiting。")


def server_loop():      
  global target

  # 判断是否有定义目标，如果没有则监听所有端口
  if not len(target):
    target = "0.0.0.0"

  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server.bind((target, port))
  server.listen(10)
  while True:
    client_socket,addr = server.accept()

    # 分拆一个线程处理新的客户端
    client_thread = threading.Thread(target=client_handler,args=(client_socket,))
    client_thread.start()

def run_command(command):
  
  # 换行
  command = command.rstrip()

  # 运行命令并讲输出返回
  try:
    output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
  except:
    output = "Failed to execute command.\r\n"

  if type(output) is str:
    output = bytes(output,encoding='utf-8')
  return output

def client_handler(client_socket):
  global upload
  global execute
  global command

  # 文件上传检测
  if len(upload_destination):

    # 读取所有的字符并写下目标
    file_buffer = ""

    while True:
      data = client_socket.recv(1024)

      if not data:
        break
      else:
        file_buffer += data

    try:
      file_descriptor = open(upload_destination,"wb")
      file_descriptor.write(file_buffer)
      file_descriptor.close()

      # 验证文件是否以写出来
      success = "Successfully saved file to " + upload_destination + "\r\n"
      client_socket.send(success.encode())
    except:
      success = "failed to  save file to " + upload_destination + "\r\n"
      client_socket.send(success.encode())
  
  # 检查命令执行
  if len(execute):

    # 运行命令
    output = run_command(execute)
    client_socket.send(output)

  # 判断是否需要一个命令行shell,如果是则进入另一个循环
  if command:
    while True:

      # 弹出一个窗口
      wininfo = b"<NC:#>"
      client_socket.send(wininfo)

      # 获取文件知道发现换行符时结束
      cmd_buffer = ""

      while "\n" not in cmd_buffer:

        bstr = client_socket.recv(1024)
        cmd_buffer += bstr.decode('utf-8')

      
      # 返回命令输出
      response = run_command(cmd_buffer)
      # 返回响应数据
      client_socket.send(response)


main()

