import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';

import Image from 'react-bootstrap/Image'
import Spinner from 'react-bootstrap/Spinner'

export default class UserProfile extends Component {
    render() {
        return (
            <Query query={USER_QUERY}>
                {({ data, loading }) => {
                    if (loading) return <Spinner animation="border" role="status" className="text-center mx-auto">
                        <span className="sr-only">Loading...</span>
                    </Spinner>;
                    const user = data;
                    return (
                        <div className="text-center mt-5">
                            <Image src={window.location.origin + '/user.png'} className="mb-5" style={{ width: "400px", height: "400px" }} roundedCircle />

                            <h2>Name: {user.me.firstName} {user.me.lastName}</h2>
                            <h2>Email: {user.me.email}</h2>
                        </div>
                    )
                }}
            </Query>
        )
    }
}

const USER_QUERY = gql`
  query getUserInfo {
    me {
        firstName
        lastName
        email
        isActive
        gid
      }
  }
`;
