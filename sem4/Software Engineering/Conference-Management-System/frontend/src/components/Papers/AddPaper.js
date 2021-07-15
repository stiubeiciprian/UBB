import React, { Component } from 'react'
import { Mutation } from 'react-apollo';
import gql from 'graphql-tag';
import PaperForm from './PaperForm';

export default class AddPaper extends Component {
  _confirm = () => {
    this.props.history.push(`/myPapers`)
  }


  render() {
    const { match } = this.props;
    console.log("addPaper conferenceId = " + match.params.id)
    return (
      <Mutation mutation={NEW_PAPER} onCompleted={() => this._confirm()}>
        {addPaper => (
          <PaperForm id={match.params.id} onSubmit={addPaper} />
        )}
      </Mutation>
    )
  }
}

const NEW_PAPER = gql`
mutation addPaper($conferenceId: String!, $abstract: Boolean!, $paperContent: String!, $title: String!){
    createPaper(input:{
      conference: $conferenceId
      abstract: $abstract
      paperContent: $paperContent
      title: $title
    }){
      paper{
        gid
        title
        user{
          email
        }
        abstract
        paperContent
      }
    }
  }
`;