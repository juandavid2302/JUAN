color= "#FF0000"

match color:
    case "#FF0000":
        print("red🔴")
    case "#00FF00":
        print("green🟢")
    case ("#0000FF"):
        print("blue🔵")
    case _:
        print("Unknown color!")