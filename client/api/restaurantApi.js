/**
 * Client API for restaurants back-end.
 */

import urljoin from 'url-join';

require('es6-promise').polyfill()
require('isomorphic-fetch');


const INDEX_URL       = 'http://localhost:5000',
      RESTAURANTS_URL = urljoin(INDEX_URL, 'restaurants');

export function getRestaurants() {
  return fetch(RESTAURANTS_URL)
    .then((response) => {
      if (response.status >= 400)
        throw new Error('Bad response from server');
      return response.json();
    });
}
