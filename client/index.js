/**
 * Entry point file.
 */

import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';

import App from 'components/App';


ReactDOM.render(
  <App />,
  document.getElementById('root')
);
