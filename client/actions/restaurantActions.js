/**
 * client/actions/restaurantActions.js
 */

import {getRestaurants} from 'api/restaurantApi';
import * as types from 'constants/ActionTypes.js';


export function loadRestaurantsSuccess(restaurants) {
  return { type: types.LOAD_RESTAURANTS_SUCCESS, restaurants };
}

export function loadRestaurants(restaurants) {
  return function(dispatch) {
    return getRestaurants().then(restaurants => {
      dispatch(loadRestaurantsSuccess(restaurants));
    }).catch(error => {
      throw(error);
    });
  }
}
