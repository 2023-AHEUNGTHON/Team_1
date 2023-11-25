// 필요한 React 모듈과 컴포넌트에서 사용할 함수들을 가져옵니다.
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

// Bootstrap의 Button 컴포넌트를 사용하기 위해 가져옵니다.
import Button from 'react-bootstrap/Button';

// Bootstrap의 CSS를 가져옵니다.
import 'bootstrap/dist/css/bootstrap.min.css';

// 해당 컴포넌트에만 적용할 CSS를 가져옵니다.
import './solution.css';

// Solution 컴포넌트를 정의합니다.
function Solution() {
  // useState 훅을 사용하여 상태를 선언합니다.
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResult, setSearchResult] = useState('');

  // react-router-dom의 useNavigate 훅을 사용하여 페이지 이동을 위한 함수를 가져옵니다.
  const navigate = useNavigate();

  // 검색을 처리하는 함수
  const handleSearch = async () => {
    try {
      // 서버에 POST 요청을 보냅니다.
      const response = await fetch('http://127.0.0.1:8000/chatgpt-api/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json', // JSON 형식의 데이터를 사용하겠다고 지정합니다.
        },
        body: JSON.stringify({ searchQuery }), // 검색어를 JSON 형식으로 변환하여 요청 본문에 추가합니다.
      });

      // 서버로부터 받은 응답을 JSON 형식으로 파싱합니다.
      const result = await response.json();

      // GPT 결과를 상태에 저장합니다.
      setSearchResult(result);

      // 검색 결과를 보여줄 페이지로 이동합니다.
      navigate('/slu_click');
    } catch (error) {
      // 오류가 발생하면 콘솔에 오류 메시지를 출력합니다.
      console.error('Error during search:', error);
    }
  };

  // JSX를 반환하여 UI를 생성합니다.
  return (
    <div className="solution">
      {/* 검색어를 입력하는 input 요소 */}
      <input
        type="text"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        placeholder="검색어를 입력하세요"
      />

      {/* Bootstrap의 Button 컴포넌트를 사용하여 버튼을 생성하고, 이 버튼 클릭 시 handleSearch 함수를 실행하도록 합니다. */}
      <Button variant="danger" className='button-slu' onClick={handleSearch}>
        {/* react-router-dom의 Link 컴포넌트를 사용하여 '/slu_click' 경로로 이동하도록 합니다. */}
        <Link to="/slu_click" className='slu_btn'>솔루션 받으러 가기</Link>
      </Button>{' '}
    </div>
  );
}

// Solution 컴포넌트를 내보냅니다.
export default Solution;