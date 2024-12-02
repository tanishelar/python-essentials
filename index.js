const moment = require('moment');
const simpleGit = require('simple-git');
const jsonfile = require('jsonfile');
const crypto = require('crypto');

const FILE_PATH = './data.json'; // Update with your file path

const randomInt = (min, max) => Math.floor(crypto.randomInt(min, max + 1));

const makeCommit = (n) => {
  if (n === 0) return simpleGit().push();

  const x = randomInt(0, 54);
  const y = randomInt(0, 6);
  const DATE = moment()
    .subtract(1, 'y')
    .add(x, 'w')
    .add(y, 'd')
    .format();

  const data = {
    date: DATE,
  };

  console.log(DATE);
  jsonfile.writeFile(FILE_PATH, data, () => {
    simpleGit()
      .add(FILE_PATH)
      .commit(DATE, { '--date': DATE }, makeCommit.bind(this, --n));
  });
};

makeCommit(50);

