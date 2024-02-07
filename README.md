# rag-demo

* Prepare
    * Copy file `.env.sample` to `.env` and fill `OPENAI_API_KEY` value 
* Run
    ```shell
    % pip install -r requirements.txt
    % python src/repo_to_vectorstore.py  
    % python src/wiki_to_vectorstore.py  
    % python src/chat.py  
     ```
* Result
    ```shell
    > T멤버십과 관련된 코드에 대해 알려줘
    이 코드는 T멤버십 할인 가격을 계산하는 기능을 가지고 있습니다. `getTmembershipDiscount`라는 정적 메소드가 있는데, 이 메소드는 제품의 가격을 입력으로 받아 그 가격의 50%를 반환합니다. 그러나 문서에는 T멤버십의 할인율이 30%라고 적혀있기 때문에, 코드와 문서 사이에는 불일치가 있는 것 같습니다.
    ```
