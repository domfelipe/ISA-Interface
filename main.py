import speech_recognition as sr
#    for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()
with sr.Microphone(device_index=1) as fonte:
  print('Reconhecendo Áudio...')
  audio = r.listen(fonte)

  texto = r.recognize_ibm(audio, language='pt-BR')

  try:
    print('Áudio Reconhecido:' + texto.capitalize())


  except sr.UnknownValueError:
    print('Áudio não reconhecido, tentando novamente...')