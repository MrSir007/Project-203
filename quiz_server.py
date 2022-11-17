import socket
import threading from Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
list_of_nicknames = []
questions = []
answers = []

def clientthread (conn, addr) :
  score = 0
  conn.send("Welcome to this quiz game!".encode("utf-8"))
  conn.send("You will receive a question. The answer to that question should be one of a, b, c, d".encode("utf-8"))
  conn.send("Good luck!\n\n".encode("utf-8"))
  index, question, answer = get_random_question_answer(conn)
  while True :
    try :
      message = conn.recv(2048).decode('utf-8')
      if message :
        if message.lower() == answer :
          score += 1
          
          conn.send(f"Bravo! Your score is {score}\n\n".encode("utf-8"))
        else :
          conn.send("Incorrect answer! Better luck next time!\n\n".encode("utf-8"))

        remove_question(index)
        index, question, answer = get_random_question_answer(conn)
    except :
      remove(conn)
      remove_nickname(nickname)

def get_random_question_answer (conn) :
  random_index = random.randint(0, len(questions) - 1)
  random_question = questions[random_index]
  random_answer = answers[random_index]
  conn.send(random_question.encode("utf-8"))
  return random_index, random_question, random_answer

def remove (conn) :
  if conn in list_of_clients :
    list_of_clients.remove(conn)

def remove_question (index) :
  questions.pop(index)
  answers.pop(index)

while True :
  conn, addr = server.accept()
  conn.send("NICKNAME".encode("utf-8"))
  nickname = conn.recv(2048).decode("utf-8")
  list_of_clients.append(conn)
  list_of_nicknames.append(nickname)
  print(nickname + "connected!")
  new_thread = Thread(target=clientthread,args=(conn,addr))
  new_thread.start()