/**
 * client/reducers/index.js
 */

import {combineReducers} from 'redux';

import restaurants from 'reducers/restaurantReducer';


const rootReducer = combineReducers({
  restaurants,
});

export default rootReducer;
