/**
 * Component Hierarchy
 * ===================
 *
 * -- RestaurantsApp [CONT]
 *    -- RestaurantList
 *       -- Restaurant
 */


import React, {Component, PropTypes} from 'react';

import Restaurant from 'components/restaurants/Restaurant';


const RestaurantList = ({restaurants}) => {
  return (
    <div>
      {
        restaurants.map(restaurant =>
          <Restaurant key={restaurant.id} restaurant={restaurant} />
        )
      }
    </div>
  );
}

RestaurantList.propTypes = {
  restaurants: PropTypes.array.isRequired,
}

export default RestaurantList;
