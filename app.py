from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def inspect_request():
    # 요청 메서드
    method = request.method
    
    # 요청 URL
    url = request.url
    
    # 요청 헤더
    headers = dict(request.headers)
    
    # 요청 쿠키
    cookies = request.cookies.to_dict()
    
    # 요청 쿼리 파라미터
    args = request.args.to_dict()
    
    # 요청 바디(JSON 혹은 raw)
    try:
        body = request.get_json(force=True)
    except:
        body = request.data.decode('utf-8')  # JSON이 아니면 raw text
    
    # 클라이언트 IP (X-Forwarded-For 포함)
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # 요청 정보를 JSON으로 반환
    info = {
        "method": method,
        "url": url,
        "client_ip": client_ip,
        "headers": headers,
        "cookies": cookies,
        "query_params": args,
        "body": body
    }
    
    return jsonify(info), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
