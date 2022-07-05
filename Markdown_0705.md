# 마크다운(MarkDown)

> 2004년 **존 그루버**가 만든 **텍스트 기반**의 가벼운 **마크업 언어**



## 마크다운 특징

- 워드프로세서는 다양한 서식과 구조를 지원하며, 문서에 **즉각적**으로 반영하는 반면

- 마크다운은 가능한 읽을 수 있또록 **최소한**의 문법으로 구조화

- **단순 텍스트 문법**으로 내용을 작성하며, 다양한 환경에서 변환하여 보여짐

  - 다양한 text editor, 웹 환경에서 모두 지원

    

#### 마크다운 활용예시

- 다양한 기술블로그에서는 **정적사이트 생성기(Static site generator)**
  - Jekyll, Gatsoy, Hugo, Hexo 등을 통해 작성된 마크다운을 HTML, CSS, JS 파일 등으로 변환하고
  - **Github pages** 기능을 통해 *호스팅(외부공개)*

* 다양한 개발환경 뿐만 아니라 일반 SW에서도 많이 사용됨



## 마크다운 문법



| 문법                                                       | EX)                                            |
| ---------------------------------------------------------- | ---------------------------------------------- |
| **Heading** : 문서의 제목이나 소제목                       | '# h1', '## h2', ~ , '###### h6'               |
| **List** : 순서가 있는(ol) 순서가 없는(ul) 리스트로 구성   | '- 리스트' , '* 리스트'                        |
| **Fenced Code block** : 코드 블록에 특정 언어 명시후 사용  | \`\`\` code \`\`\`                             |
| **Inline Code block** :  코드 블록을 특정 단어,문장에 한정 | `code` == (\`code\`)                           |
| **Link** : 하이퍼링크, 이미지 등을 연결                    | [문자열](url) == \[문자열\]\(url\)             |
| **Blockquotes** : 인용문                                   | > 문장                                         |
| **Table** : 표                                             | Lctrl + t 로 사용 행/열                        |
| **text 강조** : 굵게, 기울임, 취소선                       | Lctr + b or ** ** (굵게) , * * (기울임), ~~ ~~ |




> 참고 자료
>
> * [GitHub Flavored Markdown](https://github.github.com/gfm/)
> * [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) 
> * [Markdown Guide](https://www.markdownguide.org/)

