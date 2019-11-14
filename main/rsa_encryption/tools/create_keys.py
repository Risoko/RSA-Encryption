from rsa_encryption.tools.others_tools import (
    get_function_euler_and_module, get_public_exponent, get_private_exponent
)


def create_keys():
    """
    Method return tuple with keys:
        - first key is public
        - second key is private key
    """
    euler_and_module = get_function_euler_and_module()
    euler = euler_and_module.euler
    module = euler_and_module.module
    public_exponent = get_public_exponent(euler)
    private_exponent = get_private_exponent(public_exponent, euler)
    public_key = (public_exponent, module)
    private_key = (private_exponent, module)
    return public_key, private_key

if __name__ == "__main__":
    keys = create_keys()
    public, private = keys
    print(public)
    print(private)