/**
 * Component Hierarchy
 * ===================
 *
 * -- RestaurantsApp [CONT]
 *    -- RestaurantList
 *       -- Restaurant
 */


import React, {Component, PropTypes} from 'react';


const Restaurant = ({restaurant}) => {
  return (
    <div>
      <h1>{restaurant.name}</h1>
    </div>
  );
}

Restaurant.propTypes = {
  restaurant: PropTypes.object.isRequired,
}

export default Restaurant;
