# ....
# ....
# -- Send a response message to the client
response = "HELLO. I am the Happy Server :-)\n"

# -- The message has to be encoded into bytes
cs.send(response.encode())

# -- Close the client socket
cs.close()

#esto responde al client
#cuando nuestro server responde solo puede aceptar 1 conexion si solo esta esperando conexiones acepta varias sin problemas
#ex1 hCER QUE LO QUE MANDE EL CLIENT ES LO QUE RECIBE de nuevo
#