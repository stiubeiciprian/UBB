import React, { Component } from 'react'
import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { Link } from 'react-router-dom';
import Select from "react-dropdown-select";
import { Dropdown } from 'semantic-ui-react'

import image from '../../styles/images/image.jpg';

const USERS_QUERY = gql`
    query allUsers {
      users {
        data {
          lastName
          firstName
          gid
          password
          email
        }
      }
    }
`;

export default class Users extends Component {

  constructor(props) {
    super(props);
    this.state = { dropdownValue: "" };

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    console.log(this.state.dropdownValue)
    event.preventDefault();
  }

  handleChange = event => {
    this.setState({
      dropdownValue: event.target.value
    })

  }

  render() {
    const token = localStorage.getItem('AUTH_TOKEN')
    return (
      <main>
      <div className="homepage" style={{ textAlign: 'center', width: '100vw' }}>
        <div className="homepageText" style={{ color: 'white', width: '30vw', textAlign: 'left', paddingTop: '2em' }}>Conference management for everyone</div>
        <div className="homepageDesc" style={{ color: 'white' }}>
          A web-app designed for managing conferences, built by a group of students from UBB. Learn more <a href="/about" style={{ textDecoration: 'none', color: 'white' }}><strong>about</strong></a> our project.
        </div>
        {token &&
          <a href="/createConference"
            className="button1"
            style={{ textAlign: 'center', fontWeight: 'bold', marginTop: '9em' }}>ADD CONFERENCE
        </a>
        }
      </div>
      </main>
    )
  }
}