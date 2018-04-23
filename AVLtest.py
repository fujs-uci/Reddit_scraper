try:
        x = 0
        while(True):
                try:
                        print(x+1)
                        x += 1
                except Exception as e:
                        print("stopped, but continue loop")
except Exception as e:
        print("we stopped")
