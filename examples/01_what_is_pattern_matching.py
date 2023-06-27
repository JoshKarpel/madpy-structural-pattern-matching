# Pattern matching is about *matching* *patterns* to a *subject*.
# If one of the patterns *matches*, the code under that *case* is executed.

# match subject:
#     case <pattern_1>:
#         <action_1>
#     case <pattern_2>:
#         <action_2>
#     case <pattern_3>:
#         <action_3>
#     case _:
#         <action_wildcard>


def http_error_code_to_description(status: int) -> str:
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(f"{http_error_code_to_description(400)=}")
print(f"{http_error_code_to_description(404)=}")
print(f"{http_error_code_to_description(418)=}")
print(f"{http_error_code_to_description(472)=}")
