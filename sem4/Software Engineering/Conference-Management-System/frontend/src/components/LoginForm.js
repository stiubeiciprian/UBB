import React, { Component } from 'react';

import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'


export default class UserForm extends Component {
    state = {
        email: '',
        password: '',
    }
    handleInput = e => {
        const formData =  {};
        formData[e.target.name] = e.target.value;
        this.setState({ ...formData });
    }

    render() {
        const {onSubmit } = this.props;
        const {email, password } = this.state;
        return (
            <Form className="d-flex flex-column mt-5"
                    onSubmit={e => {
                        e.preventDefault();
                        onSubmit({
                            variables: {
                                email,
                                password,
                            }
                        }).then(() => {
                            this.setState({
                                email: '',
                                password: '',
                            });
                        }).catch(e => console.log(e));
                    }}
            >
                <h2 className="text-center">Login into your account</h2>
                <Form.Group controlId="email">
                    <Form.Label>Email:</Form.Label>
                    <Form.Control type="email" name="email" onChange={this.handleInput} value={email} placeholder="example@domain.com"/>
                </Form.Group>

                <Form.Group controlId="password">
                    <Form.Label>Password:</Form.Label>
                    <Form.Control type="password" name="password" onChange={this.handleInput} value={password}/>
                </Form.Group>

                <Button variant="primary" type="submit" className="align-self-end" className="button" style={{left: "50%", fontWeight: 'bold'}}>LOG IN</Button>
            </Form>
        )}
    }