import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import styles from "./styles.scss";
import Footer from "components/Footer";
// fetch('/notifications/')

class App extends Component {
  render() {
    return (
      <div className={styles.App}>
        <Switch>
          <Route exact path="/" render={() => "Hello!"} />
          <Route path="/login" render={() => "Login!"} />
        </Switch>
        <Footer />
      </div>
    );
  }
}

export default App;
