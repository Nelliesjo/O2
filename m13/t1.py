from flask import Flask, request

app = Flask(__name__)


@app.route('/prime_number/<num>')
def calculate_prime(num):
    num = int(num)
    is_prime = True
    for n in range(2, num):
        if num % n == 0:
            is_prime = False
            break
        else:
            is_prime = True

    answer = {
        'Number' : num,
        'isPrime' : is_prime
    }
    return answer


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)