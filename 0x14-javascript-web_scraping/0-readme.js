#!/usr/bin/env node

const { readFile } = require('fs/promises');

readFile(process.argv[2], 'utf-8')
  .then(inputD => console.log(inputD))
  .catch(err => console.error(err));
