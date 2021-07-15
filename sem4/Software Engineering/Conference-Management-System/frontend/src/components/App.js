import React, { Component } from 'react';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NewUser from './Users/NewUser';
import User from './Users/User';
import Users from './Users/Users';
import Login from './Login';
import UserProfile from './Users/Profile';
import Header from './Header';
import Conferences from './Conferences/Conferences';
import CreateConference from './Conferences/CreateConference';
import Conference from './Conferences/Conference';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/App.css';
import Logout from './Users/Logout';
import BuyTicket from './Conferences/BuyTicket';
import Orders from './Users/Orders';
import Paper from './Papers/Paper';
import AddPaper from './Papers/AddPaper';
import Reviews from './Papers/Reviews';
import MyConferences from './Conferences/MyConferences';
import MyConference from './Conferences/MyConference';
import Review from './Papers/Review';
import AssignReview from './Papers/AssignReview';
import CreateConferenceSection from './Conferences/CreateConferenceSection';
import ConferenceSchedule from './Sections/ConferenceSchedule';
import AssignSchedule from './Sections/AssignSchedule';
import { Helmet } from "react-helmet";
import About from './About';

const client = new ApolloClient({
  uri: "https://www.playgroundev.com/graphql/",
  request: (operation) => {
    const token = localStorage.getItem('AUTH_TOKEN')
    operation.setContext({
      headers: {
        authorization: token ? `JWT ${token}` : '',
      }
    })
  }
})

export default class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <Router>
          <div className="App">
            <Header />

            <Helmet>
              <meta charSet="utf-8" />
              <title>GradysBooch</title>
              <link rel="canonical" href="https://www.gradysbooch.com/" />
              <meta name="description" content="This is a conference management app build by a small team of students from UBB!" />
              <meta name="theme-color" content="#008f68" />
            </Helmet>

            <Switch>
              <Route exact path="/register" component={NewUser} />
              <Route path="/user/:id" component={User} />
              <Route path="/conference/:id" component={Conference} />
              <Route path="/home" component={Users} />
              <Route exact path="/login" component={Login} />
              <Route path="/profile" component={UserProfile} />
              <Route path="/conferences" component={Conferences} />
              <Route path="/createConference" component={CreateConference} />
              <Route path="/logout" component={Logout} />
              <Route path="/buyTicket/:id" component={BuyTicket} />
              <Route path="/orders" component={Orders} />
              <Route path="/myPapers" component={Paper} />
              <Route path="/addPaper/:id" component={AddPaper} />
              <Route path="/myReviews" component={Reviews} />
              <Route path="/myConferences" component={MyConferences} />
              <Route path="/myConference/:id" component={MyConference} />
              <Route path="/review/:id" component={Review} />
              <Route path="/assignReview/:id" component={AssignReview} />
              <Route path="/addConferenceSection/:id" component={CreateConferenceSection} />
              <Route path="/conferenceSchedule/:id" component={ConferenceSchedule} />
              <Route path="/assignSchedule/:id" component={AssignSchedule} />
              <Route path="/about" component={About} />
            </Switch>

          </div>
        </Router>
      </ApolloProvider>
    );
  }
}