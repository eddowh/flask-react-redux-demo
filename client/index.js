/**
 * Entry point file.
 */

import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';

import Root from 'containers/Root';

import {loadRestaurants} from 'actions/restaurantActions';

import configureStore from 'store/configureStore';


const store = configureStore();
store.dispatch(loadRestaurants());

ReactDOM.render(
  <Root store={store} />,
  document.getElementById('root')
);
