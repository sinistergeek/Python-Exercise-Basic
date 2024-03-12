
def make_print():
    def print_hello():
        print('hello')
    return print_hello

fn = make_print()
fn()
