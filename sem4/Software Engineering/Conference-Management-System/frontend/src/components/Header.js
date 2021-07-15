import React, { Component } from 'react';
import { withRouter } from 'react-router';

import logo from '../styles/images/Logo.png';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'

class Header extends Component {
    render() {

        const token = localStorage.getItem('AUTH_TOKEN')
        return (
            <Navbar bg="light" className="App-header" expand="md" sticky="top" fluid>
                <Navbar.Brand href="/home"><img src={logo} className="ml-2" style={{ height: 40 }} /></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto ml-auto">
                        {!token && <Nav.Link href="/login" style={{fontWeight: 'bold', marginRight: '0.9em'}}>LOGIN</Nav.Link>}
                        {!token && <Nav.Link href="/register" style={{fontWeight: 'bold'}}>REGISTER</Nav.Link>}
                        {token && <Nav.Link href="/conferences" style={{fontWeight: 'bold', color: '#414a4c', marginRight: '0.9em'}}>CONFERENCES</Nav.Link>}
                        {token && <Nav.Link href="/myPapers" style={{fontWeight: 'bold', color: '#414a4c', marginRight: '0.9em'}}>PAPERS</Nav.Link>}
                        {token && <Nav.Link href="/myConferences" style={{fontWeight: 'bold', color: '#414a4c', marginRight: '0.9em'}}>MY CONFERENCES</Nav.Link>}
                        {token && <Nav.Link href="/myReviews" style={{fontWeight: 'bold', color: '#414a4c'}}>TO REVIEW</Nav.Link>}

                    </Nav>
                    {token &&
                        <Nav className="mr-1">
                            <NavDropdown title="ACCOUNT" id="nav-dropdown" className="mr-5" style={{fontWeight: 'bold', color: 'black'}}>
                                <NavDropdown.Item href="/profile">Profile</NavDropdown.Item>
                                <NavDropdown.Item href="/orders">Orders</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="/myPapers">My papers</NavDropdown.Item>
                                <NavDropdown.Item href="/myConferences">My conferences</NavDropdown.Item>
                                <NavDropdown.Item href="/myReviews">To review</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="/logout">Logout</NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    }
                </Navbar.Collapse>
            </Navbar>
        )
    }
}

export default withRouter(Header)