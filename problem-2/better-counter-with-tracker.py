def counter():
  actions=[]
  results=[]
  count =0
  loop = True
  while loop == True:
        asw= input("Increase(i), Decrease(d), quit(q): ")

        if asw=="i":
            count= count+1
            print("Counter:", count)
            results.append(count)
            actions.append("Increase")
        elif asw == "d":
            count = count - 1
            print("Counter:", count)
            results.append(count)
            actions.append("Decrease")
        elif asw =="q":
            print("---- Counter -----:")
            print(f"Value:", count)
            print("---- Summary of actions -----:")
            aux = 0
            for action in actions:
                print(f"Action: {action} result: {results[aux]}")
                aux += 1
            break
        else:
            print("choose one correct option")

def main():
    print("Program is starting")
    counter()


if __name__ == "__main__":
    main()