# Repository Publication Checklist

Before assigning a public remote:

- [ ] Choose **private or public** visibility explicitly.
- [ ] Choose a license explicitly; do not infer one from the repository.
- [ ] Confirm `LICENSE.md`, `CITATION.cff`, and README agree.
- [ ] Create the remote under the intended owner/organization.
- [ ] Push the `main` branch.
- [ ] Confirm GitHub Actions passes.
- [ ] Confirm the canonical reproduction job passes.
- [ ] Enable Dependabot alerts/version updates if desired.
- [ ] Protect `main` if the repository will accept collaborators.
- [ ] Tag `v0.3.0`.
- [ ] Create a release from the tag.
- [ ] Record the remote URL and release commit in the post-freeze provenance ledger.
- [ ] Only then consider DOI/archival integration such as Zenodo.

The frozen Schmidt submission is historical evidence and must not be rewritten when the repository evolves.
