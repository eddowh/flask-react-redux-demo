/**
 * Main app container.
 */

import React, {Component} from 'react';
import {Provider} from 'react-redux';

import RestaurantsApp from 'containers/RestaurantsApp';


export default class Root extends Component {
  render() {
    const {store} = this.props;

    return (
      <Provider store={store}>
        <RestaurantsApp />
      </Provider>
    )
  }
}
