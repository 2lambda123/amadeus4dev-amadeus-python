from amadeus.client.decorator import Decorator


class DirectDestinations(Decorator, object):
    def get(self, **params):
        '''
        Returns airport direct routes.

        .. code-block:: python

            amadeus.airport.direct_destinations.get(
                            departureAirportCode='BLR')

        :param departureAirportCode: the IATA code of the departure airport, e.g. "BLR" for Bengaluru
        :type departureAirportCode: str
        :return: The response containing airport direct routes
        :rtype: amadeus.Response
        :raises amadeus.ResponseError: If the request could not be completed

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/airport/direct-destinations', **params)
