/**
 * Component Hierarchy
 * ===================
 *
 * -- RestaurantsApp [CONT]
 *    -- RestaurantList
 *       -- Restaurant
 */


import React, {Component, PropTypes} from 'react';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

import RestaurantList from 'components/restaurants/RestaurantList';

import * as restaurantActions from 'actions/restaurantActions';


export class RestaurantsApp extends Component {
  constructor(props, context) {
    super(props, context);
  }

  render() {
    const {restaurants} = this.props;

    return (
      <div>
        <RestaurantList restaurants={restaurants} />
      </div>
    )
  }
}

let mapStateToProps = (state, ownProps) => {
  return {
    restaurants: state.restaurants,
  };
}

let mapDispatchToProps = (dispatch) => {
  return {
    actions: bindActionCreators(restaurantActions, dispatch),
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(RestaurantsApp);
