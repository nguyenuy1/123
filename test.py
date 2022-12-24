import streamlit as st

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = st.number_input('Nhập một số:')

if is_prime(number):
    st.write(number, 'là số nguyên tố')
else:
    st.write(number, 'không phải là số nguyên tố')