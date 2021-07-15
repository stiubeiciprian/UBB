import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';

import Spinner from 'react-bootstrap/Spinner'

export default class User extends Component {
    render() {
        const { match } = this.props;
        return (
            <Query
                query={USER_QUERY}
                variables={{
                    id: match.params.id
                }}
            >
                {({ data, loading }) => {
                    if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                        <span className="sr-only">Loading...</span>
                    </Spinner>;
                    const { user } = data;
                    return (
                        <div>
                            <h1>First name: {user.firstName}</h1>
                            <h1>Last name: {user.lastName}</h1>
                            <h1>Email: {user.email}</h1>
                        </div>
                    )
                }}
            </Query>
        )
    }
}

const USER_QUERY = gql`
    query getUser($id: ID!) {
      user(id: $id) {
          lastName
          firstName
          gid
          password
          email
        }
    }
`;