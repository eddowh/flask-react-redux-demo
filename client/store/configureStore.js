/**
 * Configure store based on development environment.
 */

switch (process.env.NODE_ENV) {
  case 'production':
    module.exports = require('./configureStore.prod');

  default:
    module.exports = require('./configureStore.dev');
}

