/**
 * client/reducers/restaurantReducer.js
 */

import * as types from 'constants/ActionTypes';
import * as states from 'constants/InitialStates';


export default function restaurantReducer(state = states.RESTAURANTS, action) {
  switch(action.type) {
    case types.LOAD_RESTAURANTS_SUCCESS:
      return action.restaurants;

    default:
      return state;
  }
}
