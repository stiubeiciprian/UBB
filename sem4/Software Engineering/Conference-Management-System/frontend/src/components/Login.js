import React, { Component } from 'react'
import { Mutation } from 'react-apollo'
import gql from 'graphql-tag';
import LoginForm from './LoginForm';

const LOGIN_MUTATION = gql`
  mutation tokenAuth($email: String!, $password: String!) {
    tokenAuth(email: $email, password: $password) {
      token
    }
  }
`

export default class Login extends Component {
    _confirm = async data => {
        localStorage.setItem('AUTH_TOKEN', data.tokenAuth.token)
        console.log(localStorage.getItem('AUTH_TOKEN'))
        this.props.history.push(`/profile`)
    }

    render() {
        return (
            <div className="container">
                <Mutation mutation={LOGIN_MUTATION}
                    onCompleted={data => this._confirm(data)}
                >
                    {tokenAuth => (
                        <LoginForm onSubmit={tokenAuth} />
                    )}
                </Mutation>
            </div>
        )
    }
}