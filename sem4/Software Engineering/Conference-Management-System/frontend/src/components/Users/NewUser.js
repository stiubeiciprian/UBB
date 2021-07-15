import React, { Component } from 'react'
import UserForm from "./UserForm";
import { Mutation } from 'react-apollo';
import gql from 'graphql-tag';

export default class NewUser extends Component {

    _confirm = () => {
        this.props.history.push(`/login`)
    }

    render() {
        return (
            <div className="container">
                <Mutation mutation={NEW_USER} onCompleted={() => this._confirm()}>
                    {createUser => (
                        <UserForm onSubmit={createUser} />
                    )}
                </Mutation>
            </div>
        )
    }
}

const NEW_USER = gql`
mutation createUser($firstName: String!, $lastName: String!, $email: String!, $password: String!) {
    createUser(input:{
        firstName: $firstName
        lastName: $lastName
        password: $password
        email: $email
    }) {
      user {
        lastName
      }
    }
  } 
`;