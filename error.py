try:
    print("try")
    r = 10 / 0
    print("result = %d" % r)
except ZeroDivisionError as e:
    print("except" % e)
except ValueError as e:
    print("execpt" % e)
finally:
    print("finally")

print("END")
