let fs = require('fs');

fs.appendFile('newfilewithjs.txt', 'It is fun, right?', function (err) {
  if (err) throw err;

  console.log('완료!');
});

fs.appendFile('newfilewithjs.txt', ' It will get better in a little more time.', function (err) {
  if (err) throw err;
  console.log('수정 완료!');
});