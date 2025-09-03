try:
    print()

except ZeroDivisionError:
    print("You can't divide by zero")

except Exception as e:
    print(e)

else:
    print('ошибок нет')

finally:
    print("выполняется всегда")

exit(1)