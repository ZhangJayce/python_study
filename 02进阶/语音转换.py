import win32com.client
speaker = win32com.client.Dispatch("SAPI.SPVOICE")#调用windows 的 语音接口
speaker.Speak("zhang jayce is a good man")
