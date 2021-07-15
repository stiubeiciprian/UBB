import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default class UserForm extends Component {

    state = {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
    }

    handleInput = e => {
        const formData = {};
        formData[e.target.name] = e.target.value;
        this.setState({ ...formData });
    }

    render() {
        const { onSubmit } = this.props;
        const { firstName, lastName, email, password } = this.state;
        return (
            <Form className="mt-5 d-flex flex-column"
                onSubmit={e => {
                    e.preventDefault();
                    onSubmit({
                        variables: {
                            firstName,
                            lastName,
                            email,
                            password,
                        }
                    }).then(() => {
                        this.setState({
                            firstName: '',
                            lastName: '',
                            email: '',
                            password: '',
                        });
                    }).catch(e => console.log(e));
                }}
            >
                <h2 className="text-center pb-3">Create your account</h2>
                <Form.Group controlId="firstName">
                    <Form.Label>First name:</Form.Label>
                    <Form.Control type="text" name="firstName" onChange={this.handleInput} value={firstName} placeholder="Firstname"></Form.Control>
                </Form.Group>

                <Form.Group controlId="lastName">
                    <Form.Label>Last name:</Form.Label>
                    <Form.Control type="text" name="lastName" onChange={this.handleInput} value={lastName} placeholder="Lastname"></Form.Control>
                </Form.Group>

                <Form.Group controlId="email">
                    <Form.Label>Email:</Form.Label>
                    <Form.Control type="email" name="email" onChange={this.handleInput} value={email} placeholder="example@domain.com"></Form.Control>
                </Form.Group>

                <Form.Group controlId="firstPassword">
                    <Form.Label>Password:</Form.Label>
                    <Form.Control type="password" name="password" onChange={this.handleInput} value={password} ></Form.Control>
                </Form.Group>

                
                <div className="footer">
                    <Button variant="primary" type="submit" className="button" style={{ align: 'center', fontWeight: 'bold' }}>REGISTER</Button>
                    <br/><br/>
                    <p>Please use fictional inputs. This is only for development purpose. No email validation is being made.</p>
                </div>
            </Form>
            
        )
    }
}