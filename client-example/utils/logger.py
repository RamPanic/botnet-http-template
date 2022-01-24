
def log(msg, type_msg):

    types_messages = {

        "success": "[+]",
        "error": "[x]",
        "processing": "[*]",
        "warning": "[!]"

    }

    message = f"{types_messages[type_msg]} {msg}"

    print(message)  