const fs = require('fs');

// 파일 읽기
fs.readFile('one_number.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('파일을 읽는 중 오류가 발생했습니다:', err);
    return;
  }
  console.log('파일 내용:', data);
});

const content = 'four!';
fs.writeFile('four_number.txt', content, (err) => {
  if (err) {
    console.error('파일을 쓰는 중 오류가 발생했습니다:', err);
    return;
  }
  console.log('파일 쓰기가 완료되었습니다.');
});