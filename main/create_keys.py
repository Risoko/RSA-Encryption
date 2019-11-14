from others_tools import (get_function_euler_and_module, get_private_exponent, 
                                get_public_exponent)

def create_keys():
    euler_and_module = get_function_euler_and_module()
    euler = euler_and_module.euler
    module = euler_and_module.module
    public_exponent = get_public_exponent(euler)
    private_exponent = get_private_exponent(public_exponent, euler)
    public_key = (public_exponent, module)
    private_key = (private_exponent, module)
    print(public_key, private_key)

if __name__ == "__main__":
    create_keys()