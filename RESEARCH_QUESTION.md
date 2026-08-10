# Research Question

## Central question

Do any population-level observables provide useful prospective warning of unsafe cascades, and how does their predictive advantage change as environment and agent fidelity increase?

## Dynamic system

At time `t`:

`G_t = (V_t, E_t, X_t)`

where `V_t` is the population, `E_t` the time-varying interaction graph, and `X_t` observable state.

## Prediction target

`Y_(t+Delta) = 1` when a preregistered cascade threshold is crossed within the forecast horizon.

## Transfer retention

For a predictor `f_i` developed at fidelity/regime `i` and evaluated at `j`:

`T_(i->j) = [Q_j(f_i) - Q_j(B_j)] / [Q_i(f_i) - Q_i(B_i)]`

where `Q` is predictive performance and `B_i`, `B_j` are the same simple baseline rule evaluated in the source and target regimes, respectively. The ratio is reported only when source-regime uplift is sufficiently positive under the preregistered guard.

The v0.1 prototype evaluates this quantity only across controlled synthetic regime shifts. Transfer to real language-model agents remains an open research question.
