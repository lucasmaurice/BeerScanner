import React, { Component } from "react";

class Board extends Component {
  constructor(props) {
    super(props);
    this.state = { drinkers: [] };
  }

  async reloadAPIData() {
    clearInterval(this.interval);
    this.interval = setInterval(() => this.reloadAPIData(), 1000);
    try {
      const res = await fetch("http://localhost:8000/api/players/");
      const todoList = await res.json();
      this.setState({
        drinkers: todoList.results,
      });
    } catch (e) {
      console.log(e);
    }
  }

  componentDidMount() {
    this.reloadAPIData();
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  renderItems = () => {
    return this.state.drinkers.map((item) => (
      <tr>
        <td>
          <div>
            <span className="h4">{ item.name } </span><span className="h6"> { item.username }</span>
          </div><hr />
          Drank { item.volume }
          , in { item.reffils } reffils.
        </td>
      </tr>
    ));
  };

  render() {
    return (
      <section className="ftco-section">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-md-6 text-center mb-5">
              <span className="heading-section h2">Top Players</span>
            </div>
          </div>
          <div className="row">
            <div className="col-md-12">
              <table className="table table-borderless table-dark">
                <tbody>{this.renderItems()}</tbody>
              </table>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

export default Board;
