# template-js
A template for vanilla JavaScript projects

This template includes prettier, ESlint, and nodemon.

ESLint is configured for a dual browser/node deployment using CommonJS style `require` imports.  ESLint is configured to accomodate prettier and apply it to staged JS files.

There is also a pre-commit hook for pretty-quick.  This redundency is necessary because prettier can format files such as JSON but ESlint is not concerned with those. 
